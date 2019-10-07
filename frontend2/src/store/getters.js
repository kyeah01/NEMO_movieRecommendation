export default {
  getMovieToggle: state => state.selectedMovie.Activated,
  getMovieInfo: state => state.selectedMovie.ActivatedMovie,
  getUserTasteMovie: state => state.userData.your_taste_movie
}
