module.exports = {
  css: {
    loaderOptions: {
      sass: {
        prependData: `@import "@/styles/_variables.scss";
                      @import "@/styles/_navs.scss";
                      @import "@/styles/_movies.scss";
                      @import "@/styles/_spacing.scss";
                      @import "@/styles/_btn.scss";
                      @import "@/styles/_shared-styles.scss";`
      }
    }
  }
};
