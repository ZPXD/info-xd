# Downloads and lauches search program serverside. Searches.

server_name=$1
search_type=$2
search_phrase=$3

ssh $server_name << EOF
    git clone https://github.com/ZPXD/better_search.git
    cd better_search
    python3 search.py $search_type $search_phrase
EOF
