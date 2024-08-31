library(ggplot2)
library(png)
library(grid)

# Set the working directory to the location of your files
setwd("C:/users/Admin/Desktop/Module4Work/integration.r", encoding = "UTF-8")

# Load the PNG image
most_watched_genres_NEW <- readPNG("most_watched_genres.png")

# Check if the image was loaded successfully
if (!is.null(most_watched_genres_NEW)) {
  # Display the image
  grid.raster(most_watched_genres_NEW)
} else {
  # Handle the error
  stop("Failed to load image")
}
