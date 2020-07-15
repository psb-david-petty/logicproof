# This bash script simply executes logicproof.py with some test
# premises / goals. These are from http://intrologic.stanford.edu/

DIR="$( dirname $0 )"

# Activity 4.1 from the virtual classroom:
# https://onedrive.live.com/?authkey=%21AKEIaMjOI4GZ8gU&cid=477D5CE9111F9830&id=477D5CE9111F9830%2156158&parId=477D5CE9111F9830%2155559
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
        "w q r & => # w => (q&r)" \
        "u w p & => # u => (w&p)" \
        "s u & # s&u" \
        "q a | # q|a"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
        "p # p" \
        "p q r & => # p =>(q&r)" \
        "s r <=> # s<=>r" \
        "s # s"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-ev' \
        "q p & # (q&p)" \
        "q s | w => # (q|s) =>w" \
        "r w v | <=> # r <=> (w|v)" \
        "r # r"

# Activity 4.2 from the virtual classroom:
# https://onedrive.live.com/?authkey=%21AJj2NI3eziQneuA&cid=477D5CE9111F9830&id=477D5CE9111F9830%2156159&parId=477D5CE9111F9830%2155559
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
        "a b & p <=> # (a&b) <=> p" \
        "b s <=> # b <=> s" \
        "p s => # p => s"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
        "w p q & => # w => (p&q)" \
        "s q r | <=> # s <=> (q|r)" \
        "w s => # w => s"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
        "r p q & => # r =>(p&q)" \
        "s p w | <=> # s <=> (p|w)" \
        "r s => # r => s"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
        "r ~ s <=> # ~r<=>s" \
        "q r ~ <=> # q<=>~r" \
        "q s ~ => # q => ~s" \
        "r # r"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-ev' \
        "p # p" \
        "r q => # r=>q" \
        "w s <=> # w<=>s" \
        "r s | # r|s" \
        "w q => # w=>q" \
        "p q & # p&q"

# Activity 4.3 from the virtual classroom:
# https://onedrive.live.com/?authkey=%21AL2JfVYrc8l6-NE&cid=477D5CE9111F9830&id=477D5CE9111F9830%2156368&parId=477D5CE9111F9830%2155559

/usr/bin/env python3 ${DIR}/../src/logicproof.py '-ev' \
	"s r &       # (S&R)" \
	"a b s ~ & =># A=>(B&~S)" \
	"a ~         # ~A"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
	"a b &       # (a&b)" \
	"p q a ~ & =># p=>(q&~a)" \
	"p ~         # ~p"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
	"r s w & =>      # r => ( s & w )" \
	"w r <=>         # w <=> r" \
	"r ~ ~           # ~~r" \
	"w q =>          # w => q" \
	"s q & r <=>     # ( s & q ) <=> r"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
	"r m & s w & =>         # (r&m)=>(s&w)" \
	"r m & a & s w & b | => #  (r&m&a)=>(s&w|b)"

# Activity 4.4 from the virtual classroom:
# https://onedrive.live.com/?authkey=%21ALcQGP2kXq6u8uw&cid=477D5CE9111F9830&id=477D5CE9111F9830%2156552

/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
    "p q =>         # p=>q" \
    "p q |          # m=> (p|q)" \
    "m q =>         # m=>q"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
    "p q r => =>    # (p=>(q=>r)" \
    "p q => p r => =># (p=>q) => (p=>r)"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
    "p q p => =>    # p=>(q=>p)"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
    "p q =>         # p=>q" \
    "s r <=>        # s<=>r" \
    "s q =>         # s=>q" \
    "m s =>         # m=>s" \
    "p r | m |      #  p|r|m" \
    "q m r s & <=> |# (q | (m<=>(r&s)))"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-ev' \
    "r s q p & | |  # (r|s|(q&p))" \
    "m r <=>        # m<=>r" \
    "q s <=>        # q<=>s" \
    "q m =>         # q=>m" \
    "m              # m"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
    "p q |  # (p|q)" \
    "p ~    # ~p" \
    "q      # q"
/usr/bin/env python3 ${DIR}/../src/logicproof.py '-e' \
    "p q => # p=>q" \
    "p ~ q |# (~p|q)"

/usr/bin/env python3 ${DIR}/../src/logicproof.py '-ev' \
	"--help"
