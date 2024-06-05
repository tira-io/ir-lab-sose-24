<template>
  <div @mouseover="make_this_run_active(true)" @mouseleave="make_this_run_active(false)">
    <h3>{{ title }}</h3>
    <br>
    
    <diff-ir 
      :docs="topic_details['docs']" :run="serp_run" :ir_dataset="this.run.split('____')[0]" v-if="topic_details"/>
  </div>
</template>

<script lang="ts">
import { get } from '@/utils'
import topics from '@/ir_datasets';
import DiffIr from '@/components/DiffIr.vue'

export default {
  name: "serp",
  props: ['run', 'topic', 'run_id', 'reference_run_id', 'topic_details'],
  components: {DiffIr},
  data() {
    return {
      ranking: [{'doc_id': '1', 'relevance': 1, 'color': 'green'}, {'doc_id': '2', 'relevance': 0, 'color': 'red'}, {'doc_id': '3', 'relevance': 'U', 'color': 'grey'}],
      cache: {
        'run-details.jsonl': {'start: 0 end: 100': {'runs': [{'name': 'does not exist', "P@10": 0.3, "nDCG@10": 0.203, "Judged@10": 0.3, 'relevance': ['U', '0', '1'], "docs": [{'doc_id': '1', 'doc_id_to_offset': {'start': 0, 'end': 0}}]}], 'dataset': '1', 'qid': '1'}}
      }
    }
  },
  methods: {
    make_this_run_active(active) {
      if(active && this.reference_run_id != this.run) {
        this.$emit('activate_run', this.run);
      }
    }
  },
  computed: {
    title() {
      return this.run.split('____')[1].split('/')[2]
    },
    serp_docs() {
      return {'1': {'relevance': 1, 'snippet': 'doc 1: foo', 'weights': []}, '2': {'relevance': 0, 'snippet': 'doc 2: tmp 1', 'weights': []}, '3': {'relevance': 2, 'snippet': 'doc 3: tmp 2', 'weights': [(1,3,1)]}}
    },
    serp_run() {
      //return [{'rank': 1, 'score': 3, 'doc_id': '1'}, {'rank': 2, 'score': 2, 'doc_id': '3'}, {'rank': 23, 'score': 1, 'doc_id': '2'}]
      for (let i of this.topic_details['runs']) {
        if (i['name'] == this.run.split('____')[1]) {
          console.log(i)
          return i['ranking'];
        }
      }

      return []
    },
    topic_data() {
      let expected_dataset = this.run.split('____')[0]
      for (let t of topics.default) {
        if (t.dataset == expected_dataset) {
          return t
        }
      }
    },
    ranking_2() {
      let entry = this.cache['run-details.jsonl'][this.topic_data['run_details']['start'] + '-' + this.topic_data['run_details']['end']]
      let run_id = this.run.split('____')[1]
      if (entry) {
        for (var run of entry['runs']) {
          if (run['name'] == run_id) {
            let ret = [...run['docs']]
            for (let i in ret) {
                ret[i]['color'] = 'grey'

                if (parseInt(run['relevance'][i]) > 0) {
                    ret[i]['color'] = 'green'
                }
                if (parseInt(run['relevance'][i]) <= 0) {
                    ret[i]['color'] = 'red'
                }
            }

            return ret
          }
        }
      }

      return []
    }
  }
}
</script>
