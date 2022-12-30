#include <iostream>
#include <vector>
namespace Trees {
    template<typename KeyT, typename Comp = std::less<KeyT>>
    class SearchTree {
        struct Node // внутренний узел
        {
            Node *parent_, *left_,  *right_;
            KeyT key_;
            //int height;
            Node(Node * l = nullptr, Node * r = nullptr, Node * p = nullptr):
                left_(l), right_(r), parent_(p) {}
            Node(const KeyT& val,Node * p, Node * l = nullptr, Node * r = nullptr):
                left_(l), right_(r), key_(val),parent_(p) {}
            private:
            Node(){};

        };
        using iterator = Node *; // положение внутри дерева
        Node *top_;
    public: //constr
        SearchTree(): top_{nullptr} {}
        ~SearchTree(){
            //if(!top_) return;
            Node * buf = top_;
            unsigned short curr_is = -1; // -1 - top, 0 current is left, 1 current is right
            while(buf){
                if(buf->left_ == nullptr && buf->right_ == nullptr){
                    std::cout << buf->key_<<std::endl; // for tests 00
                    Node * prev = buf->parent_;
                    delete buf;
                    buf = prev;
                    if(!buf) return;
                    if(curr_is == 0){
                        buf->left_ = nullptr;
                    }
                    if(curr_is == 1){
                        buf->right_ = nullptr;
                    }
                    continue;
                }
                if(buf->left_ == nullptr && buf->right_ != nullptr){
                    buf = buf->right_;
                    curr_is = 1;
                    //std::cout << "Destr 0 1"<<std::endl;
                    continue;
                }
                if(buf->left_ != nullptr && buf->right_ == nullptr){
                    buf = buf->left_;
                    curr_is = 0;
                    //std::cout << "Destr 1 0"<<std::endl;
                    continue;
                }
                if(buf->left_ != nullptr && buf->right_ != nullptr) {
                    buf = buf->left_;
                    curr_is = 0;
                    //std::cout << "Destr 1 1"<<std::endl;
                }
            }
        }
    public: // селекторы
        iterator lower_bound(KeyT key) const;

        iterator upper_bound(KeyT key) const;

        int distance(iterator fst, iterator snd) const;

    public: // модификаторы
        void insert(KeyT key){
            if(top_ == nullptr){
                top_ = new Node(key, nullptr);
                std::cout << "top\n";
                return;
            }
            Node * buf = top_;      // indecator
            Node * current = buf;   // parent for new el
            while(buf){
                if(key == buf->key_) return;
                if(Comp{}(key, buf->key_)) {
                    current = buf;
                    buf = buf->left_;
                }
                else{
                    current = buf;
                    buf = buf->right_;
                }
            }
            if(Comp{}(key, current->key_)){
                current->left_ = new Node{key, current};
                //std::cout << "left\n";
            }
            else{
                current->right_ = new Node{key, current};
                //std::cout << "right\n";
            }


        }
        bool contains(KeyT key){
            Node* buf = top_;
            while(buf){
                if(key == buf->key_){
                    return true;
                }
                if(Comp{}(key, buf->key_)){
                    buf = buf->left_;
                }
                else{
                    buf = buf->right_;
                }
            }
            return false;
        }
    };
}
using namespace Trees;
int main() {
    SearchTree<int> a;
    std::vector<int> test = {5, 4, 1, 7, 6, 9};
    for(int &i:test){
        a.insert(i);
    }
    std::cout << a.contains(-3) << a.contains(21)  << a.contains(3) << " "<< a.contains(7) << " "<< a.contains(9)<< " "<< a.contains(6)<< " "<< a.contains(1)<< " "<< a.contains(4)<< " "<< a.contains(5)<<"\n";
}
