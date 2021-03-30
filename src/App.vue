<template>
  <div id="app">
    <People v-bind:people="people"/>
  </div>
</template>

<script>
import People from './components/People'

export default {
  name: 'App',
  components: {
    People
  },
  
  data() {
    return {
      people: [
        {
          id: 1,
          name: "Mark",
          share: 50
        },
        {
          id: 2,
          name: "Traian",
          share: 50
        }
      ]
    }
  }
}
</script>

<style>
#app {
  font-family: Montserrat;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app::-webkit-scrollbar {
  display: none;
}
</style>
