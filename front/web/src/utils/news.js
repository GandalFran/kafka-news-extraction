module.exports = {
  newsSentiment: function(compound) {
    if (compound < 0.5 && compound > -0.5) {
      return 'neutral';
    } else if (compound > 0.5) {
      return 'positive';
    } else {
      return 'negative';
    }
  }
};
