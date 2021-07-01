<template>
<div>
  <div class="hello ">
   <div>
    
  
    <header class="bg-white shadow">
      <div class="">
        <h1 class="">
          To do List
        </h1>
      </div>
    </header>

    <main>

        <div class="container">
        <div class="row">
        <div class="col-md-10 mx-4">
        <table class="table ">
          <thead>
            <tr>
              <th>CheckMark Done</th>
              <th>Task Name</th>
              <th>Edit</th>
              <th>Delete</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(task, index) in tasks" :key="index">
            <td>
                <input type="checkbox" v-model="task.done">
              </td>

                  <td class="">
                  <div class="">

                    <div class="">
                      <div class="">
                        {{ task.title }}
                      </div>

                    </div>
                  </div>
                </td>


                <td class="">
                  <a href="#" class=""  @click="editTask(task)">Edit</a>
                </td>
               <td class="">
                  <a href="#" class=""   @click="onDeleteTask(taks)">Delete</a>
                </td>
              </tr>
          </tbody>
        </table>
        </div>
        </div>
                <div class="panel panel-default col-md-10 mx-4">
          <h2 class="text-center">Add A new Task</h2>
          <form v-on:submit="addTask" class="app-form">
              <input type="text" class="form-control" v-model="tasks.title">
              <input type="submit" value="Add" class="btn btn-block btn-primary">
          </form>
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


a {
  color: #42b983;
}
</style>

