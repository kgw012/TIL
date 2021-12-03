import java.util.Scanner;

class Solution{
    public static void main(String[] args){
        int C_COST = 1;
        int Q_COST = 2;

        Scanner sc = new Scanner(System.in);

        int T = Integer.parseInt(sc.nextLine());

        for(int t = 1; t <= T; t++){
            String st = sc.nextLine();
            
            // 천지인 자판 확인
            int OFFSET = (int)'a';
            char prev = st.charAt(0);
            int c_cnt = ((int)prev - OFFSET) % 3 + 1;

            for(int i = 1; i < st.length(); i++){
                char c = st.charAt(i);
                if( ((int)prev - OFFSET) / 3 == ((int)c - OFFSET) / 3 ){
                    c_cnt++;
                }

                c_cnt += ((int)c - OFFSET) % 3 + 1;
                prev = c;
            }

            int c_cost = c_cnt * C_COST;

            // 쿼티 자판 확인
            int q_cnt = st.length();
            int q_cost = q_cnt * Q_COST;

            // 대소 비교 후 정답 출력
            if(c_cost < q_cost) {
                System.out.printf("#%d %s\n", t, "CHEONJIIN");
            } else if(c_cost > q_cost) {
                System.out.printf("#%d %s\n", t, "QWERTY");
            } else{
                System.out.printf("#%d %s\n", t, "DRAW");
            }
        }

        sc.close();
    }
}
