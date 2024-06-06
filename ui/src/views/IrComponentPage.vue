<template>
  <h1>IR Components</h1>
</template>

<script lang="ts">
import { extractFromUrl, uniqueElements, updateUrl } from "@/utils"
import { data_access } from "@/ir_datasets"
import topics from '@/ir_datasets';


export default {
  components: {},
  data: () => ({
    datasets: Object.keys(data_access),
  }),
  methods: {
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
  }
}
</script>
