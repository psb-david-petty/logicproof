# This bash script simply executes logicproof.py with some test
# premises / goals. These are from http://intrologic.stanford.edu/

# Activity 4.3 from the virtual classroom:
# https://onedrive.live.com/?authkey=%21AL2JfVYrc8l6-NE&cid=477D5CE9111F9830&id=477D5CE9111F9830%2156368&parId=477D5CE9111F9830%2155559

DIR="$( dirname $0 )"
/usr/bin/env python3 ${DIR}/../src/logicproof.py "-v" \
	"s r &       # (S&R)" \
	"a b s ~ & =># A=>(B&~S)" \
	"a ~         # ~A"
/usr/bin/env python3 ${DIR}/../src/logicproof.py \
	"a b &       # (a&b)" \
	"p q a ~ & =># p=>(q&~a)" \
	"p ~         # ~p"
/usr/bin/env python3 ${DIR}/../src/logicproof.py \
	"r s w & =>      # r => ( s & w )" \
	"w r <=>         # w <=> r" \
	"r ~ ~           # ~~r" \
	"w q =>          # w => q" \
	"s q & r <=>     # ( s & q ) <=> r"
/usr/bin/env python3 ${DIR}/../src/logicproof.py \
	"r m & s w & =>         # (r&m)=>(s&w)" \
	"r m & a & s w & b | => #  (r&m&a)=>(s&w|b)"
/usr/bin/env python3 ${DIR}/../src/logicproof.py \
	"--help"


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
