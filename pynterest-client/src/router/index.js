import Vue from 'vue'
import Router from 'vue-router'

import Header from '../components/base_components/Header'

Vue.use(Router)
const router = new Router(
  {
    mode: history,
    routes: {
      path: '/',
      components: {
        header: Header
      }
    }
  }
)

router.beforeEach((to, from, next) => {
  console.log('to', to);
  console.log('from', from);
})

export default router
