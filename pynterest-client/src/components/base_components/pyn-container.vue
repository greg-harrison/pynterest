<template>
  <div class="pyn-container">
    <PynCard
      v-for="(pyn, index) in pyns"
      v-bind:pyn="pyn"
      v-bind:index="index"
      v-bind:key="pyn.pyn_id"
    />
  </div>
</template>

<script>
import PynCard from "../pyn_components/pyn-card";

export default {
  data() {
    return {
      pyns: [
        {
          pyn_id: "b93bfdcd-3507-40d6-9778-71d008197b9d",
          title: "Test",
          url: "http://www.testing.org",
          description: "A test",
          imageUrl: "http://via.placeholder.com/236x150"
        },
        {
          pyn_id: "b93bfdcd-3507-40d6-9778-71d008197b9c",
          title: "Test",
          url: "http://www.testing.org",
          description: "A test",
          imageUrl: "http://via.placeholder.com/236x150"
        },
        {
          pyn_id: "b93bfdcd-3507-40d6-9778-71d008197b9e",
          title: "Test",
          url: "http://www.testing.org",
          description: "A test",
          imageUrl: "http://via.placeholder.com/236x150"
        }
      ]
    };
  },
  components: {
    PynCard
  }
};
</script>

<style lang="scss">
.pyn-container {
  display: inline-flex;
  margin-top: 3rem;
}
</style>
