export default {
  selectedMovie : ( state, payload ) => {
    if (payload) {
      state.selectedMovie.Activated = true
    } else {
      state.selectedMovie.Activated = false
    }
    state.selectedMovie.ActivatedMovie = payload
  },
}
