<template>
<div>
  <h3>Topic {{topic.query_id}} ({{topic.dataset}})</h3>
  
  <b>Title: </b> {{title}}<br>
  <b>Description: </b> {{description}}<br>
  <b>Narrative: </b> {{narrative}}<br>
</div>
</template>
    
<script lang="ts">
  import { execute_get } from '@/utils'

  export default {
    name: "topic-details",
    props: ['topic'],
    watch: {
      topics(newValue) {this.fetchData()},
    },
    data() {
      return {
        title: '',
        description: '',
        narrative: ''
      }
    },
    methods: {
      fetchData() {
        this.title = ''
        this.description = ''
        this.narrative = ''
        if(this.topic['topic_details']['end']) {
          execute_get('topic-details.jsonl', this.topic['topic_details']['start'] + '-' + this.topic['topic_details']['end']).then(i => {
            this.title = i['default_text']
            this.description = i['description']
            this.narrative = i['narrative']
          });
        }
      },
    },
    beforeMount() {
      this.fetchData();
    }
  }
</script>
    