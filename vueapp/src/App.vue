<template>
  <div id="app" class="flex items-center justify-center row">
    <div class="col-12">
    <button @click="showModal = true" class="bg-transparent border border-green-500 hover:border-green-500 text-gray-700 hover:text-green-500 font-bold py-2 px-4 rounded-md">
            Add Task
        </button>

    <TaskCreation :show="showModal"  @close="showModal=false" @update="$refs.HelloWorld.getTasks()"> </TaskCreation>
    </div>

    <div class="col-12">
    <HelloWorld msg="Welcome to Your Vue.js App" ref="HelloWorld"/>
    </div>


  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import TaskCreation from "./components/TaskCreation.vue"

export default {
  name: 'App',
  components: {
    HelloWorld,
    TaskCreation
  },

        data() {
            return {
                showModal: false
            }
        }
}
</script>




<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
