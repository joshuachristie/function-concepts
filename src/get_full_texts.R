library('fulltext')
library('dplyr')
## read in dois into a vector
references <- read.csv(file='/home/joshua/Downloads/output.csv', header=FALSE, sep=",")
dois <- references[-1, ] %>% pull(V29) %>% as.vector()
## randomize dois
set.seed(42)
## dois <- dois[sample(1:length(dois))]
dois <- dois[sample(1:50)]
## set output location
fulltext::cache_options_set(full_path='/home/joshua/Downloads/func3d_texts')
refs <- ft_get(dois)
