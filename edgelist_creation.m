function [E] = edgelist_creation(num_graphs,num_nodes,density)
%quick function to create random weighted edgelists for testing
%saves to csv file for reading into python program

%INPUT:
%num_graphs: number of desired graph edgelists to produce
%num_nodes: number of nodes in each graph (i.e. all will have same number)
%density: int from 1 to 100 indicating the desired edge density pct of graph

%OUTPUT:
%each edgelist will be saved in a csv file with the name in the format of:
% E[numnodes]_[density]_[id].  E.g. E25_10_1 is an edgelist for a 25 node,
% 10 pct density graph and is given the ID 1.  ***Existing Files with the
% same name will be overwritten***

    %create edgelists with desired number of nodes and density
    E = cell(num_graphs,1);
    for i = 1:num_graphs
        A = create_adjacency(num_nodes,150,density);
        E{i} = create_edgelist(A);
    end
    
    %save Edgelists to csv text file
    for i = 1:num_graphs
        filename = strcat('E',num2str(num_nodes),'_',num2str(density),'_',num2str(i),'.csv');
        csvwrite(filename,E{i}) 
    end
end

function [A] = create_adjacency(num_nodes,max_weight,density)
%creates sparse adjacency matrix with an *approximate* density as specified
%all elements are integers, graph is undirected (symmetric adjacency)
    A = sprandsym(num_nodes, density/100 );
    A(A~=0) = randi(max_weight,nnz(A),1);
end

function [E] = create_edgelist(A)
%Takes adjacency matrix A as input, returns 3 column vector of edges
%E = [start,end, weight]
    [u,v,w] = find(A);
    E = [u,v,w];
end