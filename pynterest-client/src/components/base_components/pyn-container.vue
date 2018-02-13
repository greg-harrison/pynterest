<template>
  <div class="pyn-container">
    <span>
    -- Infinitely scroll and build out pyn-card components  --
    </span>
    <PynCard />

  </div>
</template>

<script>
import PynCard from "../pyn_components/pyn-card";

export default {
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
