<template>
  <div class="header-container">
    <div class="header-container_title">
    {{title}}
    </div>
    <div class="header-container-panel_right">
      <!-- If is logged in show USERNAME and a link to the PROFILE -->
      <!-- else - Show the LOGIN button -->
      <a href="">Login</a>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "PY"
    };
  }
};
</script>

<style lang="scss">
// Header is Sticky

.header-container {
  vertical-align: middle;
  position: absolute;
  clear: both;
  width: 100%;
  height: 3rem;
  line-height: 3rem;
  background-color: white;
  border-bottom: 1px solid grey;
  .header-container_title {
    padding-left: 1rem;
    float: left;
  }
  .header-container-panel_right {
    text-align: right;
    margin-right: 1rem;
  }
}
</style>
