#include <iostream>

using namespace std;

int main()
{
    int size  = 6;
    int q = size;
    int threads = 4;
    
    int q_boof = 1;
    int p_boof = 1;
    size_t co = 0;
    size_t step = size/threads +  (size % threads == 0 ? 0 : 1) ;
    cout << "step: "<<step << endl;
    while(true){
      cout << "    test: "<<p_boof <<" " << q_boof<<" "<<co<<endl;
        if(co == step && q_boof != q){
            // do func
            cout << p_boof << " "<<q_boof <<endl;
            p_boof = q_boof;
            p_boof++;
            co = 0;
        }
        if(q_boof == q){
            //do func
          cout << p_boof << " "<<q_boof <<endl;
            break;
        }
      
        q_boof++;
        co++;
    }
  }
