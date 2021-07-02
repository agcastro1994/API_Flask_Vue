<script>

import TaskEdition from "./TaskEdition.vue"

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
                  <a href="#" class="text-indigo-600 hover:text-indigo-900"   @click="onDeleteTask(task.id)">Delete</a>
                 </div>
                  </div>
                </td>
              </tr>

</template>