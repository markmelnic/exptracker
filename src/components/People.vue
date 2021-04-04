<template>
    <table>
        <th>
            Person
        </th>
        <th>
            Share
        </th>
        <th>
            DELETE
        </th>
    <tr v-bind:key="person.id" v-for="person in people">
        <td>{{person.name}}</td>
        <td>{{person.share}}%</td>
        <td>
            <button v-on:click="delUser(person.id)">REMOVE</button>
        </td>
    </tr>
    </table>

    <input v-model="name" placeholder="Name" required />
    <input v-model="share" placeholder="Share %" required />
    <button @click.prevent="addUser(id)">ADD</button>

</template>

<script>
import { greq, preq, dreq } from '@/areq.js';

export default {
    name: "People",
    data() {
        return {
            people: null,
            id: null,
            name: null,
            share: null
        }
    },
    methods: {
        async addUser() {
            this.people = await preq('people', {name: this.name, share: this.share})
            this.name = ""
            this.share = ""
        },
        async delUser(id) {
            this.people = await dreq('people', {'id': id})
        }
    },
    created: async function() {
        this.people = await greq('people')
    }
}
</script>

<style scoped lang="scss">
table {
    width: 20em;
    border: solid 1px black;
    td {
        counter-reset: 2;
    }
}
tr, th, td {
    border: solid 1px black;
}
</style>
