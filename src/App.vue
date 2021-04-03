<template>
  <div id="app">
    <h1>Extracker</h1>
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
  methods: {
  },
};
</script>

<style>
#app {
  font-family: Montserrat;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  width: fit-content;
  margin: 0 auto 0 auto;

  font-size: 18px;
}

#app::-webkit-scrollbar {
  display: none;
}

h1 {
  color: #214FF1;
}
</style>
