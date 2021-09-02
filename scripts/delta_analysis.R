library(ape)
source("code.R") #Script found in the GitHub of this delta method. https://github.com/mrborges23/delta_statistic/blob/master/code.R

#function for each cluster (n is the number) calculating the Delta and p value
analysis <- function(n) {
  tree <- read.tree(file=paste("tree_cluster_",n,".nw", sep="")) #common ancestor tree for the LBD cluster members
  data <- read.csv(paste("cluster_",n,"_members.csv", sep="")) #list of leaves of the tree having the LBD 
  data <- data[match(tree$tip.label, data$taxID),]
  trait <- data$cluster
  #delta
  deltaA <- delta(trait,tree,0.1,0.0589,10000,10,100)
  #p_value 
  random_delta <- rep(NA,100)
  for (i in 1:100){
   rtrait <- sample(trait)
   random_delta[i] <- delta(rtrait,tree,0.1,0.0589,10000,10,100)
  }
  p_value <- sum(random_delta>deltaA)/length(random_delta)
  print(deltaA)
  print(p_value) 
  analysis_ <- p_value
  write.csv(paste(n, p_value, sep="\t"),  file=paste("output_",n,".txt",sep=""))
}

#Calculation of the values for cluster_n
analysis(n)