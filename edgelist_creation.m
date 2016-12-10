function [] = edgelist_creation()
%quick function to create random weighted edgelists for testing
%saves to csv file for reading into python program

%create graphs with different numbers of nodes
A25_10 = create_adjacency(25,150,.1); %25 nodes, ~10% edges
A25_50 = create_adjacency(25,150,.5); %25 nodes, ~50% edges
A50_10 = create_adjacency(50,150,.1); %50 nodes
A50_50 = create_adjacency(50,150,.5);

%create edgelists
E25_10 = create_edgelist(A25_10);
E25_50 = create_edgelist(A25_50);
E50_10 = create_edgelist(A50_10);
E50_50 = create_edgelist(A50_50);

%write to csv
csvwrite('E25_10.csv',E25_10);
csvwrite('E25_50.csv',E25_50);
csvwrite('E50_10.csv',E50_10);
csvwrite('E50_50.csv',E50_50);

end

function [A] = create_adjacency(num_nodes,max_weight,density)
%creates sparse adjacency matrix with an *approximate* density as specified
%all elements are integers, graph is undirected (symmetric adjacency)
    A = sprandsym(num_nodes, density );
    A(A~=0) = randi(max_weight,nnz(A),1);
end

function [E] = create_edgelist(A)
%Takes adjacency matrix A as input, returns 3 column vector of edges
%E = [start,end, weight]

    [u,v,w] = find(A);
    E = [u,v,w];

end