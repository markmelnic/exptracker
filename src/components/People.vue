<template>
    <table>
        <th>
            Person
        </th>
        <th>
            Share
        </th>
    <tr v-bind:key="person.id" v-for="person in people">
        <td>{{person.name}}</td>
        <td>{{person.share}}%</td>
    </tr>
    </table>
</template>

<script>
export default {
    name: "People",
    props: ["people"]
}
</script>

<style scoped lang="scss">
table {
    border: solid 1px black;
    td {
        counter-reset: 2;
    }
}
tr, th, td {
    border: solid 1px black;
}
</style>
