<template>
  <v-toolbar density="compact" title="IR Lab SoSe 2024">
    <v-tabs v-if="!is_mobile">
      <v-tab to="/ir-lab-sose-24/">About</v-tab>
      <v-tab to="/ir-lab-sose-24/milestones">Milestones</v-tab>
      <v-tab to="/ir-lab-sose-24/topics">Browse Topics</v-tab>
      <v-tab to="/ir-lab-sose-24/components">Browse Components</v-tab>
      <!--<v-tab to="/ir-lab-sose-24/docs">Browse Documents</v-tab>-->
      <v-tab to="/ir-lab-sose-24/runs">Browse Runs</v-tab>
    </v-tabs>
    <v-menu v-if="is_mobile">
      <template v-slot:activator="{ props }">
        <v-btn icon="mdi-menu" v-bind="props"></v-btn>
      </template>
      <v-list>
        <v-list-item to="/ir-lab-sose-24/">About</v-list-item>
        <v-list-item to="/ir-lab-sose-24/milestones">Milestones</v-list-item>
        <v-list-item to="/ir-lab-sose-24/topics">Browse Topics</v-list-item>
        <v-list-item to="/ir-lab-sose-24/components">Browse Components</v-list-item>
        <!--<v-list-item to="/ir-lab-sose-24/docs">Browse Documents</v-list-item>-->
        <v-list-item to="/ir-lab-sose-24/runs">Browse Runs</v-list-item>
      </v-list>
    </v-menu>
  </v-toolbar>
  <router-view />
</template>

<script lang="ts">
import {ref} from 'vue'
import {is_mobile} from "@/main";

export default {
  data: () => ({
    text: 'loading...',
    is_mobile: is_mobile(),
  }),
  computed: {
    currentRouteName() {
      return this.$route;
    },
    urlSuffix() {
      return (ref(window.location).value.href + '?').split('?')[1]
    }
  }
}
</script>
