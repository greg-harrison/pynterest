<template>
  <div :title=pyn.description class="card pyn-card mr-1 mb-1">
    <a :href="pyn.url">
      <img :src="pyn.imageUrl" alt="img" class="card-img-top">
      <div class="card-body p-0">
        <h5 class="card-title pt-1 pb-1 m-0">{{pyn.title}}</h5>
        <div class="card-text d-sm-none">{{pyn.description}}</div>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  props: ["pyn", "index", "key"],
  data: function() {
    return {
      pyn: this.pyn,
      index: this.index,
      key: this.key
    };
  }
};
</script>

<style lang="scss">
.pyn-card {
  a {
    cursor: pointer;
    text-decoration: none;
  }
}
</style>
