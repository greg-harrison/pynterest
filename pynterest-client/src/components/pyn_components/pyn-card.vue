<template>
  <div class="card pyn-card">
    <a :href="pyn.url">
      <img :src="pyn.imageUrl" alt="img" class="card-img-top">
      <div class="card-body p-0">
        <h5 class="card-title">{{pyn.title}}</h5>
        <div class="card-text">{{pyn.description}}</div>
      </div>
    </a>
  </div>
</template>

<script>
// imageUrl
// title
// URL for ahref
// description for hover??
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
