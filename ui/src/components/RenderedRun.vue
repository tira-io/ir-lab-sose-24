<template>
    <h3>Topic {{topics[0].query_id}} ({{topics[0].dataset}})</h3>
  
    <v-data-table v-model="selected_runs" :items="filtered_runs" show-select hover dense>
      <template v-slot:item.relevance="{ item }">
        <dense-run-overview :judgments="item.relevance" />
      </template>
    </v-data-table>
  </template>
    
  <script lang="ts">
    import { get } from '@/utils'
    import DenseRunOverview from './DenseRunOverview.vue'
    
    export default {
      name: "run-details",
      props: ['topics'],
      components: {DenseRunOverview},
      watch: {
        topics(newValue) {this.fetchData()},
      },
      data() {
        return {
          cache: {'run-details.jsonl': {'start: 0 end: 100': {'runs': [{'name': 'does not exist', "P@10": 0.3, "nDCG@10": 0.203, "Judged@10": 0.3, 'relevance': ['U', '0', '1']}]}}},
          selected_runs: null
        }
      },
      methods: {
        fetchData() {
          for (var topic of this.topics) {
            get(topic['run_details'], this)
          }
        },
      },
      computed: {
      },
      beforeMount() {
        this.fetchData();
      }
    }
    </script>
    