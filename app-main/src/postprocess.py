import re
from ast import literal_eval
from nltk.tokenize import sent_tokenize

def get_model_json(output):
	#) res_d = dict(map(str.strip, line.split(':', 1)) for line in output.splitlines()[:6])
	res_d = {}
	for line in output.splitlines()[:6]:
		splits = line.split(":", 1)
		if len(splits) > 2:
			splits = [splits[0], "".join(splits[1:])]
		try:
			field, text = splits
			res_d[field] = text.strip()
		except:
			field, text = "ERROR", "ERROR"
		res_d[field] = text.strip()

	n_res_d = {}
	for f_name, text in res_d.items():
		new_k = f_name.replace("'", "")
		if new_k in ["Achievements", "Passive Language"]:
			try:
				new_v = literal_eval(text)
			except:
				new_v = text
		else:
			new_v = text
		n_res_d[new_k] = new_v
	return n_res_d


def post_processing(output: str):
	eos_list = ["### Evaluation:","\#", "#", "\['", "'\]", "\{'", "'\}", "<|eot_id|>", "\n", "\\n", "--", "##", "###", "\|", "|","\\n\\n"]
	sentence_exp = [" I ", "I'm", "let's", "Let’s", "Let me"]
	
	eos_list = [i.lower() for i in eos_list]
	sentence_exp = [i.lower() for i in sentence_exp]

	## BOS
	# lines = []
	# verify = True
	# for line_n, line in enumerate(output.splitlines()):
	# 	if verify:
	# 		if "<|eot_id|>" in line:
	# 			continue
	# 		elif "assistant" in line:
	# 			continue
	# 		elif "### Instruction:":
	# 			continue
	# 		elif line=="":
	# 			continue
	# 		else:
	# 			verify = False
	# 	else:
	# 		lines.append(line)

	# output = "\n".join(lines)
	
	## EOS
	eos_p = re.compile("|".join(eos_list))

	text = output.lower()
	start = None
	for res in re.finditer(eos_p, text):
		start = res.start()
		break
	if start:
		output = output[:start].strip()
	else:
		output = output.strip()
	output = output.rsplit(".", 1)[0] + "."

	## Sentences:
	final_sents = []
	for sent in sent_tokenize(output):
		add_sent = True
		text = sent.lower()
		for exp in sentence_exp:
			if exp in text:
				add_sent = False
	
		if add_sent:
			final_sents.append(sent)
	final_output = " ".join(final_sents)
	return final_output

def model_output(output: str, model_n: int):
	output = output.split("### Response:\n")[1] if "### Response:\n" in output else output
	output = output.split("### Response:")[1] if "### Response:" in output else output
	output = output.rsplit(".", 1)[0] + "."

	if model_n in [4, 6]:
		output_json = get_model_json(output)
		if 'Screen Out' in output_json.keys():
			output_json['Screen Out'] = post_processing(output_json['Screen Out'])
		else:
			print(output_json)
		output = output_json
	else:
		output = post_processing(output)
	return output

def adjust_passive(ouput_json_4, output_json_6):
	passive_lang = output_json_6.get("Passive Language", "")
	if isinstance(passive_lang, list):
		ouput_json_4["Passive Language"] = output_json_6.get("Passive Language", "")
	return ouput_json_4