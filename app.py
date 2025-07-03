from flask import Flask, request, jsonify

app = Flask(__name__)

def is_valid_cpf(cpf: str) -> bool:
    """Valida um CPF (apenas dígitos, sem formatação)."""
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # Cálculo do primeiro dígito verificador
    sum_ = sum(int(cpf[i]) * (10 - i) for i in range(9))
    first_digit = (sum_ * 10) % 11
    if first_digit == 10:
        first_digit = 0
    
    # Cálculo do segundo dígito verificador
    sum_ = sum(int(cpf[i]) * (11 - i) for i in range(10))
    second_digit = (sum_ * 10) % 11
    if second_digit == 10:
        second_digit = 0
    
    return cpf[-2:] == f"{first_digit}{second_digit}"

@app.route('/validate-cpf', methods=['POST'])
def validate_cpf():
    data = request.get_json()
    cpf = data.get('cpf', '').replace('.', '').replace('-', '')
    return jsonify({"valid": is_valid_cpf(cpf)})
    
# Nova rota GET
@app.route('/validate-cpf/<string:cpf>', methods=['GET'])
def validate_cpf_get(cpf):
    cleaned_cpf = cpf.replace('.', '').replace('-', '')
    return jsonify({"valid": is_valid_cpf(cleaned_cpf)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)