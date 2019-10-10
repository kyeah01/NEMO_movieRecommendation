export default {
  selectedMovie : ( state, payload ) => {
    if (payload) {
      state.selectedMovie.Activated = payload.varified
    } else {
      state.selectedMovie.Activated = false
    }
    state.selectedMovie.ActivatedMovie = payload
  },
  setMovieSearchList(state, payload) {
    state.movieSearchList = payload.map(m => m)
  },
  setProfileSearch(state, payload) {
    state.userData = payload
  },
  setAuthUser(state, {
    authUser,
    isAuthenticated
  }) {
    Vue.set(state, 'authUser', authUser)
    Vue.set(state, 'isAuthenticated', isAuthenticated)
  },
  updateToken(state, newToken) {
    // TODO: For security purposes, take sessionStorage out of the project.
    sessionStorage.setItem('token', newToken);
    state.jwt = newToken;
  },
  removeToken(state) {
    // TODO: For security purposes, take localStorage out of the project.
    sessionStorage.removeItem('token');
    state.jwt = null;
  }
}
