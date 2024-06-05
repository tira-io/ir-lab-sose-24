<template>
  <p class="justify-center mx-2 mb-5">
  The <a href="https://github.com/tira-io/teaching-ir-with-shared-tasks/tree/main#courses" target="_blank">courses</a> are roughly in four milestones, with a task, supporting material, and one deliverable per milestone.
  </p>
  <div>
    <v-row class="justify-center mx-2 mb-5">
      <v-col :cols="columns" v-for="task in tasks">
        <v-row>
          <v-menu>
            <template v-slot:activator="{ props }">
              <v-card class="ma-1 w-100 text-start" :max-width="max_width" color="gray" variant="tonal">
                <v-card-item>
                  <span class="text-h6 mb-1">{{task.milestone}}</span>
                  <span style="font-size: .7em;">&nbsp;&nbsp;(Deadline: {{task.deadline}})</span>
                </v-card-item>
              </v-card>
            </template>
          </v-menu>

          <v-menu>
            <template v-slot:activator="{ props }">
              <v-card class="ma-1 w-100 text-start" :max-width="max_width" color="blue" variant="tonal">
                <v-card-item>
                  <span class="text-h6 mb-1">Task:<br> {{task.title}}</span>
                </v-card-item>
              </v-card>
            </template>
          </v-menu>

          <v-menu>
            <template v-slot:activator="{ props }">
              <v-card class="ma-1 w-100 text-start" :max-width="max_width" color="light-gray" variant="tonal">
                <v-card-item>
                  <span class="text-h6 mb-1">Support Material:<br></span>
                  <ul>
                    <li v-for="m in task.supporting_material">
                      <a :href="m.link" target='_blank'>{{m.title}}</a>
                    </li>
                  </ul>
                </v-card-item>
              </v-card>
            </template>
          </v-menu>

          <v-menu>
            <template v-slot:activator="{ props }">
              <v-card class="ma-1 w-100 text-start" :max-width="max_width" color="green" variant="tonal">
                <v-card-item>
                  <span class="text-h6 mb-1">Deliverable:<br></span>
                  {{task.deliverable}}
                  
                </v-card-item>
              </v-card>
            </template>
          </v-menu>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import {is_mobile} from "@/main";

export default {
  name: "milestones",
  data() {
    return {
      tasks: [
        {
          'milestone': 'Milestone 1',
          'deadline': '22.04.2024',
          'title': 'Formulate topics',
          'supporting_material': [
            {'title': 'ir_datasets browser', 'link': 'https://tira-io.github.io/ir-dataset-browser/'},
            {'title': 'ir_datasets Tutorial', 'link': 'https://github.com/tira-io/teaching-ir-with-shared-tasks/blob/main/tutorials/tutorial-ir-datasets.ipynb'}
          ],
          'deliverable': 'Topics file'
        },

        {
          'milestone': 'Milestone 2',
          'deadline': '06.05.2024',
          'title': 'Acquire relevance judgments',
          'supporting_material': [
            {'title': 'Annotation platform', 'link': 'https://doccano.web.webis.de/'},
            {'title': 'ir_datasets browser', 'link': 'https://tira-io.github.io/ir-dataset-browser/'}
          ],
          'deliverable': 'Qrels file'
        },

        {
          'milestone': 'Milestone 3',
          'deadline': '01.07.2024',
          'title': 'Develop IR system',
          'supporting_material': [
            {'title': 'Evaluation platform', 'link': 'https://www.tira.io/task-overview/ir-lab-sose-2024'},
            {'title': 'Web IDE + Tutorials', 'link': 'https://github.com/tira-io/teaching-ir-with-shared-tasks/tree/main/tutorials'}
          ],
          'deliverable': 'System submission'
        },

        {
          'milestone': 'Milestone 4',
          'deadline': '14.07.2024',
          'title': 'Conduct statistical analyses',
          'supporting_material': [
            {'title': 'Evaluation platform', 'link': 'https://www.tira.io/task-overview/ir-lab-sose-2024'},
            {'title': 'Tutorial notebook', 'link': 'https://github.com/tira-io/teaching-ir-with-shared-tasks/tree/main/tutorials'}
          ],
          'deliverable': 'Report'
        },
      ],
    }
  },
  computed: {
    columns() {
      if(is_mobile()) {
        return 12
      }

      return 3
    },
  }
}
</script>
