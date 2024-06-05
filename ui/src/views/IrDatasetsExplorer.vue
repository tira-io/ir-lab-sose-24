<template>
  <div class="d-flex">
    <v-data-table v-model="selected_topics" :items="filtered_topics" item-value="dataset_id_and_query_id" :headers="filtered_headers" show-select hover dense>
    <template v-slot:header.dataset="{ header }">
      <v-autocomplete clearable label="Filter datasets &hellip;" prepend-inner-icon="mdi-magnify" variant="underlined" v-model="dataset_filter" multiple :items="uniqueElements(topics, 'dataset')"/>
      Dataset
    </template>
    <template v-slot:header.query_id="{ header }">
      <v-autocomplete clearable label="Filter number &hellip;" prepend-inner-icon="mdi-magnify" variant="underlined" v-model="topic_num_filter" multiple :items="queries_for_autocomplete"/>
      Num
    </template>
    <template v-slot:header.default_text="{ header }">
      <v-text-field clearable label="Filter queries &hellip;" prepend-inner-icon="mdi-magnify" variant="underlined" v-model="query_filter"/>
      Query
    </template>
    <template v-slot:footer.prepend>
        <v-select menu-icon="mdi-cog" variant="plain" v-model="selected_headers" item-title="name" item-value="value" :items="available_headers" hide-headers multiple style="max-width: 100px;" class="ma-2">
          <template v-slot:selection="{ item, index }"/>
        </v-select>
      </template>
    </v-data-table>
  </div>


  <div class="d-flex" v-if="!selected_topics">
    Please select topics for browsing in the table above.
  </div>

  <div v-if="selected_topics && selected_topics.length > 0">
    <h3 class="text-h3">Browse {{ selected_topics.length }} Topics</h3>

    <v-expansion-panels v-model="tab" multiple>
      <v-expansion-panel>
        <v-expansion-panel-title>Details</v-expansion-panel-title>
        <v-expansion-panel-text>
          <v-row class="justify-center mx-2">
            <v-col :cols="columns" v-for="selected_topic in selected_topics">
              <topic-details :topic="filtered_topics_map[selected_topic]" />
            </v-col>
          </v-row>
          
        </v-expansion-panel-text>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-title>
          Relevance Judgments 
          <!--(ToDo: Deep Link here)-->
        </v-expansion-panel-title>
        <v-expansion-panel-text>
          <v-row class="justify-center mx-2">
            <v-col :cols="columns" v-for="selected_topic in selected_topics">
              <qrel-details :selected_qrel_headers="selected_qrel_headers" :topics="[filtered_topics_map[selected_topic]]" />
            </v-col>
          </v-row>
          <!--<h3>TODO: Add visualization(s) and implement the dummy columns.</h3>-->
          <v-select menu-icon="mdi-cog" variant="plain" v-model="selected_qrel_headers" item-title="name" item-value="value" :items="available_qrel_headers" hide-headers multiple style="max-width: 100px;" class="ma-2">
            <template v-slot:selection="{ item, index }"/>
          </v-select>
        </v-expansion-panel-text>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-title>Runs</v-expansion-panel-title>
        <v-expansion-panel-text>
          <v-row class="justify-center mx-2">
            <v-col :cols="columns" v-for="selected_topic in selected_topics">
              <run-details :topics="[filtered_topics_map[selected_topic]]"/>
            </v-col>
          </v-row>

          <!--<h3>TODO: Add visualization as in the ir_measures explorer using the Relevance vector from the table above.</h3>-->
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script lang="ts">
import topics from '@/ir_datasets';
import {extractFromUrl, updateUrl, uniqueElements, filter_topics} from "@/utils";
import {is_mobile} from "@/main";
import RunDetails from '@/components/RunDetails.vue';
import QrelDetails from '@/components/QrelDetails.vue';
import TopicDetails from '@/components/TopicDetails.vue';

export default {
  name: "ir-datasets-explorer",
  components: {RunDetails, QrelDetails, TopicDetails},
  data() {
    return {
      topic_num_filter: extractFromUrl('topic'),
      dataset_filter: extractFromUrl('dataset'),
      query_filter: extractFromUrl('query'),
      tab: null,
      selected_topics: null,
      topics: topics.default,
      selected_headers: is_mobile() ? ['dataset', 'default_text'] : ['dataset', 'query_id', 'default_text', 'max_nDCG@10', 'median_nDCG@10', 'min_nDCG@10'],
      available_headers: [
        {name: 'Dataset', value: 'dataset'},
        {name: 'Topic', value: 'query_id'},
        {name: 'Query', value: 'default_text'},
        {name: 'nDCG@10 (Minimum)', value: 'min_nDCG@10'},
        {name: 'nDCG@10 (Median)', value: 'median_nDCG@10'},
        {name: 'nDCG@10 (Maximum)', value: 'max_nDCG@10'},
        {name: 'nDCG@10 (Variance)', value: 'var_nDCG@10'},
        {name: 'Judged@10 (Minimum)', value: 'min_Judged@10'},
        {name: 'Judged@10 (Median)', value: 'median_Judged@10'},
        {name: 'Judged@10 (Maximum)', value: 'max_Judged@10'},
        {name: 'Judged@10 (Variance)', value: 'var_Judged@10'},
        {name: 'Precision@10 (Minimum)', value: 'min_P@10'},
        {name: 'Precision@10 (Median)', value: 'median_P@10'},
        {name: 'Precision@10 (Maximum)', value: 'max_P@10'},
        {name: 'Precision@10 (Variance)', value: 'var_P@10'},
      ],
      headers: [
        { title: 'Dataset', value: 'dataset', sortable: false},
        { title: 'Num', value: 'query_id', sortable: false},
        { title: 'Query', value: 'default_text', sortable: false},
        { title: 'nDCG@10', value: 'nDCG@10', align: 'center', children: [{title: 'Minimum', value: 'min_nDCG@10', sortable: true}, { title: 'Median', value: 'median_nDCG@10', sortable: true}, { title: 'Maximum', value: 'max_nDCG@10', sortable: true}, { title: 'Variance', value: 'var_nDCG@10', sortable: true}]},
        { title: 'Judged@10', value: 'Judged@10', align: 'center', children: [{ title: 'Minimum', value: 'min_Judged@10', sortable: true}, { title: 'Median', value: 'median_Judged@10', sortable: true}, { title: 'Maximum', value: 'max_Judged@10', sortable: true}, { title: 'Variance', value: 'var_Judged@10', sortable: true}]},
        { title: 'Precision@10', value: 'P@10', align: 'center', children: [{ title: 'Minimum', value: 'min_P@10', sortable: true}, { title: 'Median', value: 'median_P@10', sortable: true}, { title: 'Maximum', value: 'max_P@10', sortable: true}, { title: 'Variance', value: 'var_P@10', sortable: true}]},
      ],


      available_qrel_headers: [
        {name: 'Document', value: 'doc_id'},
        {name: 'Relevance', value: 'relevance'},
        {name: 'Retrieved (Top 10)', value: 'retrieved_in_10'},
        {name: 'Retrieved (Top 100)', value: 'retrieved_in_100'},
        {name: 'Median Rank', value: 'median_rank'}
      ],
      selected_qrel_headers: is_mobile() ? ['doc_id', 'relevance', 'median_rank'] : ['doc_id', 'relevance', 'median_rank', 'retrieved_in_100'],
    }
  },
  methods: {
    updateFilter() {
      updateUrl(this.topic_num_filter, this.dataset_filter, this.query_filter);
    },
    uniqueElements(element: any[], key: string) {
      return uniqueElements(element, key)
    },
    is_mobile() {
      return is_mobile()
    }
  },
  beforeMount() {
    for (let t of this.topics) {
      t['dataset_id_and_query_id'] = t['dataset'] + '____' + t['query_id']
    }
  },
  watch: {
    topic_num_filter: function () { this.updateFilter() },
    dataset_filter: function () { this.updateFilter() },
    query_filter: function () { this.updateFilter() },
  },
  computed: {
    filtered_topics() {
      return filter_topics(this.topics, this.topic_num_filter, this.dataset_filter, this.query_filter)
    },
    queries_for_autocomplete() {
      return uniqueElements(filter_topics(this.topics, null, this.dataset_filter, this.query_filter), 'query_id');
    },
    filtered_topics_map() {
      return this.topics.reduce((map, obj) => {
        map[obj.dataset_id_and_query_id] = obj;
        return map;
      }, {});
    },
    columns() {
      if(is_mobile()) {
        return 12
      }

      return Math.floor(12 / this.selected_topics.length)
    },
    filtered_headers() {
      let headers = this.headers
      if (this.selected_headers.length > 0) {
        headers = headers.filter(header => this.selected_headers.includes(header.value))
      }
      var add_separator = false
      for (let header of this.headers) {
        header = {...header}
        if (!header.children) {
          continue
        }
        header.children = header.children.filter(child => this.selected_headers.includes(child.value))

        if (header.children.length > 0) {
          if (add_separator) {
            headers.push({title: '', value: header.value + '_sep', sortable: false})
          }
          add_separator = true

          headers.push(header)
        }
      }

      return headers
    }
  }
}
</script>
