<template>

    <div v-if="show[0]" class="modal fixed w-full h-full top-0 left-0 flex items-center justify-center">
        <div @click.self="exit_modal()" class="modal-overlay absolute w-full h-full bg-gray-900 opacity-50"></div>

        <div class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto">


            <div class="modal-content py-4 text-left px-6">

                <div class="flex justify-center items-center pb-3">
                    <p class="text-2xl font-bold text-center">Editando la tarea con id: {{show[1].id}}</p>
                </div>

                <form class="mt-6">

                    <div>
                        <label for="title" class="block text-sm text-gray-800 dark:text-gray-200">Title</label>
                        <input type="text" v-model="title" class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
                    </div>


                    <div class="mt-6">
                      <a href="#">
                        <span class="m-2  " @click="close_modal(show[1])">Edit Task</span>
                        </a>

                    </div>


                </form>

            </div>
        </div>
    </div>

</template>

<script>
import axios from "axios";
    export default {
        name: "TaskEdition",

        props: {
            show: Boolean
        },
        data() {
            return{
                 title: " "
            }
        },



        methods:{
            async close_modal(task) {
               const path = 'http://localhost:5000/task/'+task.id;
                if (this.title != " ") {
                 const res = await axios.put(path, {"title": this.title, "finished": task.finished });
                 this.result = res.status;
                   }
                  this.$emit("update")

                this.$emit("close")
            },

            exit_modal(){
                this.$emit("update")

                this.$emit("close")
            }

        }
    }
</script>