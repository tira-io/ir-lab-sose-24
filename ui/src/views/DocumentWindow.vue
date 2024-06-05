<template>
<v-dialog width="90%" height="90%" v-model="dialogVisible">
  <template v-slot:activator="{ props }">
    <a href="javascript:void(0)" v-bind="props" v-if="'' + toggle == 'undefined'">{{ doc_id }}</a>
  </template>

  <template v-slot:default="{ isActive }">
    <v-card :title="doc_id + ' (' + dataset + ')'">
      <v-card-text> {{text}}</v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text="Close" @click="isActive.value = false"/>
      </v-card-actions>
    </v-card>
  </template>
</v-dialog>
</template>

<script lang="ts">
import { execute_get } from "@/utils"
import { data_access } from "@/ir_datasets"

export default {
  name: "document-window",
  props: ['doc_id', 'dataset', 'start', 'end', 'toggle'],
  watch: {
    toggle(newValue) {
      this.dialogVisible = true;
    },
    dialogVisible(visible) {
      if(visible) {
        this.fetchData()
      }
    },
  },
  data() {
    return {
      text: '',
      dialogVisible: false,
    }
  },
  methods: {
    fetchData() {
      this.text = ''
      execute_get(data_access.documents[this.dataset], this.start + '-' + (this.end -1)).then((i) => this.text = i['text']);
    },
  },
  beforeMount() {
    if ('' + this.toggle !== 'undefined') {
      this.dialogVisible = true
    }
  }
}
</script>