python3 ../src/logicproof.py "-v" \
	"s r &       # (S&R)" \
	"a b s ~ & =># A=>(B&~S)" \
	"a ~         # ~A"
python3 ../src/logicproof.py \
	"a b &       # (a&b)" \
	"p q a ~ & =># p=>(q&~a)" \
	"p ~         # ~p"
python3 ../src/logicproof.py \
	"r s w & =>      # r => ( s & w )" \
	"w r <=>         # w <=> r" \
	"r ~ ~           # ~~r" \
	"w q =>          # w => q" \
	"s q & r <=>     # ( s & q ) <=> r"
python3 ../src/logicproof.py \
	"r m & s w & =>         # (r&m)=>(s&w)" \
	"r m & a & s w & b | => #  (r&m&a)=>(s&w|b)"
python3 ../src/logicproof.py \
	"--help"
