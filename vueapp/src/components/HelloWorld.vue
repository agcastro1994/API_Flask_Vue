<template>
<div>
  <div class="hello ">
   <div>
    
  
    <header class="bg-white shadow">

    </header>

        <main>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="col-12">
         <button @click="showModal = true" class="bg-transparent border border-green-500 hover:border-green-500 text-gray-700 hover:text-green-500 font-bold py-2 px-4 rounded-md">
            Add Task
        </button>

        <TaskCreation :show="showModal"  @close="showModal=false" @update="getTasks()"> </TaskCreation>

    </div>

        <div class="px-4 py-6 sm:px-0">
          <div class="flex flex-col">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
        <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-green-100">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                CheckMark Done
                </th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Task Name
              </th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Edit
              </th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Delete
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">

            <TaskItem v-for="(task, index) in tasks" :key="index" :task="task" @update="getTasks()"></TaskItem>

          </tbody>
        </table>
        </div>
        </div>



        </div>
        </div>
        </div>
        </div>

    </main>


  </div>
  </div>
</div>
</template>

<script>
import axios from "axios";

import TaskCreation from "./TaskCreation.vue"
import TaskItem from "./TaskItem.vue"

export default {
  name: "Tasks",

    components: {
    TaskCreation,
    TaskItem


  },

   data() {
    return {
      tasks: [],
      message: '',
      showMessage: false,
      showModal: false,



    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {

          console.error(error);
        });
    },





},
created() {
    this.getTasks();
  }
}
</script>



<style scoped>


a {
  color: #42b983;
}
</style>

