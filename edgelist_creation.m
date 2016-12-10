function [] = edgelist_creation()
%quick function to create random weighted edgelists for testing
%right now just creates a few quick complete graphs to test
%saves to csv file for reading into python program


%create complete graphs
A25_c = create_adjacency(25,25*24/2); %25 nodes, complete edges
A50_c = create_adjacency(50,50*49/2); %50 nodes, complete edges
A100_c = create_adjacency(100,100*99/2); %100 nodes, complete edges
A200_c = create_adjacency(200,200*199/2); %200 nodes, complete edges


%create edgelists
E25_c = create_edgelist(A25_c);
E50_c = create_edgelist(A50_c);
E100_c = create_edgelist(A100_c);
E200_c = create_edgelist(A200_c);

csvwrite('E25_c.csv',E25_c);
csvwrite('E50_c.csv',E50_c);
csvwrite('E100_c.csv',E100_c);
csvwrite('E200_c.csv',E200_c);

end

function [A] = create_adjacency(num_nodes,num_edges)
    max_edges = num_nodes*(num_nodes-1)/2;
    
    if num_edges > max_edges  
        error('Too many edges -- more than complete graph')
    else
        A = randi(num_nodes,num_nodes);
        A(logical(eye(size(A)))) = 0; %zero out the diagonal, no self-edges
        
        removals = max_edges - num_edges;
        for i = 1:removals
            %remove as many edges as requested by zeroeing weight
            u = randi(num_nodes);
            v = randi([1:u-1,u+1:num_nodes]); %avoid diagonal coordinates
            A(u,v) = 0;
        end
    end
end

function [A] = remove_edges(A,num_removals)
    
    for i = 1:num_removals
        u = randi(num_nodes);
        v = randi([1:u-1,u+1:num_nodes]); %avoid diagonal coordinates
        A(u,v) = 0;
    end

end

function [E] = create_edgelist(A)
    E = zeros(nnz(A),3);
    edge_cnt = 1;
    num_nodes = size(A,1);
    for i = 1:num_nodes
        for j = 1:num_nodes
            weight = A(i,j);
            if weight~=0
                E(edge_cnt,:) = [i,j,weight];
                edge_cnt = edge_cnt +1;
            end
        end
        
    end

end