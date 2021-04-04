<template>
  <div id="app">
    <header>
      <img alt="Extracker Logo" src="./assets/logo.png">
      <h1>Extracker</h1>
    </header>
    <People/>
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

header {
  display: flex;
  flex-direction: row;

  padding: 2em 0 1em 0;
}

img {
  height: 2em;
  filter: invert(21%) sepia(95%) saturate(3684%) hue-rotate(228deg) brightness(96%) contrast(98%);
}

h1 {
  font-size: 2em;
  font-weight: 500;
  line-height: 1em;
  color: #214FF1;
  margin: 0 0 0 .1em;
}
</style>
