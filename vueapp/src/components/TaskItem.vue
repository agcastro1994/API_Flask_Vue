<script>

import TaskEdition from "./TaskEdition.vue"
import axios from "axios"

  export default {
    props: ['task'],
     components: {
     TaskEdition

  },
    data () {
      return {
        editing: false,
         showModalEdit: false,
      }
    },

     methods:{
            reload() {
        this.$emit("update")
        },
        async deleteTask(id){
             const res = await axios.delete('http://localhost:5000/task/' + id);
             this.result = res.status;
             this.reload()

        }
        }
  }
</script>

<template>

            <tr>
             <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900">
                        <input type="checkbox" v-model="task.done">
                       </div>
                 </div>
                 </div>
                </td>

                  <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900">
                        {{ task.title }}
                      </div>

                    </div>
                  </div>
                </td>


                <td class="px-4 py-4 whitespace-nowrap text-center text-sm font-medium">
                <div class="flex items-center">
                <div class="ml-0">
                  <button @click="showModalEdit=true" class="bg-transparent border border-green-500 hover:border-green-500 text-gray-700 hover:text-green-500 font-bold py-2 px-4 rounded-md">
                    Edit
                  </button>

                    <TaskEdition :show="[showModalEdit, task]"  @close="showModalEdit=false" @update="reload()"> </TaskEdition>

                  </div>
                  </div>
                </td>
               <td class="px-4 py-4 whitespace-nowrap text-center text-sm font-medium">
               <div class="flex items-center">
                <div class="ml-0">
                 <button @click="deleteTask(task.id)"  class="bg-transparent border border-green-500 hover:border-green-500 text-gray-700 hover:text-green-500 font-bold py-2 px-4 rounded-md">
                    Delete
                  </button>
                 </div>
                  </div>
                </td>
              </tr>

</template>