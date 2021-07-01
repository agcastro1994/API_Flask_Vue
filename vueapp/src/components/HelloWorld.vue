<template>
<div>
  <div class="hello ">
   <div>
    
  
    <header class="bg-white shadow">

    </header>

        <main>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">

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
            <tr v-for="(task, index) in tasks" :key="index">
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
                  <a href="#" class="text-indigo-600 hover:text-indigo-900"  @click="editTask(student)">Edit</a>
                  </div>
                  </div>
                </td>
               <td class="px-4 py-4 whitespace-nowrap text-center text-sm font-medium">
               <div class="flex items-center">
                <div class="ml-0">
                  <a href="#" class="text-indigo-600 hover:text-indigo-900"   @click="onDeleteTask(student)">Delete</a>
                 </div>
                  </div>
                </td>
              </tr>
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

export default {
  name: "Tasks",
  
   data() {
    return {
      tasks: [],

      message: '',
      showMessage: false,

      /*addStudentForm: {
        firstname: '',
        lastname: '',
        gender: '',
        age: '',
        paid: [],
      },
      
      editForm: {
        id: '',
        firstname: '',
        lastname: '',
        gender: '',
        age: '',
        paid: [],
      },
     */
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
          // eslint-disable-next-line
          console.error(error);
        });
    }
  
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

