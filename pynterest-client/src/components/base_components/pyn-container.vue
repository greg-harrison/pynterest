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
      // We'll generate the image at 236x150 ALWAYS to avoid breaking the UI like this
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
        },
        {
          pyn_id: "b93bfdcd-3507-40d6-9778-71d008197b9f",
          title: "Test",
          url: "http://www.testing.org",
          description: "A test",
          imageUrl: "http://via.placeholder.com/236x250"
        },
        {
          pyn_id: "b93bfdcd-3507-40d6-9778-71d008197b9g",
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
  flex-wrap: wrap;
  margin-top: 3rem;
}
</style>
