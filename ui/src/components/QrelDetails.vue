<template>
  <h3>Topic {{topics[0].query_id}} ({{topics[0].dataset}})</h3>
  <Bar :data="chartData" />
  
  <v-data-table :items="filtered_qrels" :headers="filtered_headers" hover dense>
    <template #item.doc_id="{ item }">
      <document-window :doc_id="item.doc_id" :dataset="item.dataset" :start="item.doc_id_to_offset.start" :end="item.doc_id_to_offset.end" />
    </template>
  </v-data-table>
</template>
    
<script lang="ts">
  import { get } from '@/utils'
  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  import DocumentWindow from '../views/DocumentWindow'


    export default {
      name: "qrel-details",
      props: ['topics', 'selected_qrel_headers'],
      components: {Bar, DocumentWindow},
      watch: {
        topics(newValue) {this.fetchData()},
        selected_qrel_headers(newValue) {this.fetchData()},
      },
      data() {
        return {
          cache: {'qrel-details.jsonl': {'0-100': {'qrels': [{"qid": "93", "relevance": 1, "doc_id": "182", "retrieved_by": "?? / ??", "median_rank": "??", "var_rank": "??"}]}}},
          available_headers: [
            {title: 'Document', value: 'doc_id', sortable: true},
            {title: 'Relevance', value: 'relevance', sortable: true},
            {title: 'Median Rank', value: 'median_rank', sortable: true},
            {title: 'Retrieved (Top 10)', value: 'retrieved_in_10', sortable: true},
            {title: 'Retrieved (Top 100)', value: 'retrieved_in_100', sortable: true},
          ]
        }
      },
      methods: {
        fetchData() {
          for (var topic of this.topics) {
            get(topic['qrel_details'], this)
          }
        },
      },
      computed: {
        chartData() {
          let ret = {}
          for (let qrel of this.filtered_qrels) {
            if (!ret[qrel['relevance']]) {
              ret[qrel['relevance']] = 1
            }

            ret[qrel['relevance']] += 1
          }

          return {
            labels: [''],
            datasets: Object.entries(ret).map(([k, v]) => {
              return {label: k, backgroundColor: '#f87979', data: [v]}
            })
          }
        },
        filtered_qrels() {
          let ret = []
  
          for (let topic of this.topics) {
            let entry = this.cache['qrel-details.jsonl'][topic['qrel_details']['start'] + '-' + topic['qrel_details']['end']]
            if (entry) {
              if (topic['dataset'] != entry['dataset']) {
                  throw new Error('dataset mismatch')
              }
  
              if (topic['query_id'] != entry['qid']) {
                  throw new Error('query_id mismatch')
              }
  
              for (var qrel of entry['qrels']) {
                qrel = {...qrel}
                qrel['dataset'] = topic['dataset']
                qrel['query_id'] = topic['query_id']
                ret.push(qrel)
              }
            }
          }
  
          return ret;
        }, filtered_headers() {
          return this.available_headers.filter((i) => this.selected_qrel_headers.includes(i.value))
        }
      },
      beforeMount() {
        this.fetchData();
      }
    }
    </script>
    