<template>
  <v-row class="ma-2">
    <v-col cols="4">
      <v-autocomplete clearable label="Select dataset &hellip;" v-model="ir_dataset" :items="uniqueElements(topics, 'dataset')"/>
    </v-col>
    <v-col cols="4">
      <v-text-field clearable :disabled="!ir_dataset" label="Document IDs (comma seperated) &hellip;" v-model="doc_ids"/>
    </v-col>

    <v-col cols="4">
      <v-btn block size="large" :disabled="!ir_dataset || !doc_ids" color="primary" @click="load_document_id">Load</v-btn>
    </v-col>
  </v-row>

  <v-row class="ma-2" v-if="ir_dataset && (!texts || !texts[ir_dataset] || !texts[ir_dataset][doc_id_iter[0]] || texts[ir_dataset][doc_id_iter[0]] == 'loading...')">
    <v-col cols="4"/>
    <v-col cols="4">Example Document ID: {{ Object.keys(texts[ir_dataset])[0] }}</v-col>
    <v-col cols="4"/>
  </v-row>

  <v-divider v-if="texts[ir_dataset]"/>

  <div v-if="document_end && doc_id">
   <document-window :doc_id="doc_id" :dataset="ir_dataset" :start='document_start' :end="document_end" :toggle="document_window_visible"/>
  </div>
</template>

<script lang="ts">
import { extractFromUrl, uniqueElements, updateUrl } from "@/utils"
import { load_document_offsets } from "@/random_document_access"
import { data_access, example_documents } from "@/ir_datasets"
import DocumentWindow from '../views/DocumentWindow'
import topics from '@/ir_datasets';


export default {
  components: {DocumentWindow},
  data: () => ({
    topics: topics.default,
    ir_dataset: extractFromUrl('dataset'),
    doc_ids: extractFromUrl('doc_ids'),
    example_doc_id: '<TBD>',
    texts: {...example_documents.default},
    document_start: null,
    document_end: null,
    doc_id: null,
    document_window_visible: true,
  }),
  methods: {
    async load_document_id() {
      updateUrl(null, this.ir_dataset, null, this.doc_ids);

      if (!(this.ir_dataset in data_access.databases)) {
        this.ir_dataset = null;
      }

      if (!(this.ir_dataset in this.texts)) {
        this.texts[this.ir_dataset] = {}
      }

      for (let doc_id of this.doc_id_iter) {
        if (this.ir_dataset && doc_id /*&& !(doc_id in this.texts[this.ir_dataset])*/
        ) {
          load_document_offsets(this.ir_dataset, doc_id).then(i => {
            this.document_start = i['start']
            this.document_end = i['end']
            this.doc_id = doc_id
            this.document_window_visible = this.document_window_visible + 'a'
          })
        }
      }
    },
    uniqueElements(element: any[], key: string) {
      return uniqueElements(element, key)
    },
  },
  computed: {
    doc_id_iter() {
      return this.doc_ids ? this.doc_ids.split(',') : []
    },
  },
  watch: {
    ir_dataset: function () { this.load_document_id() }
  },
  beforeMount() {
    this.load_document_id();
  },
}
</script>
