from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def generate_sql_query(question, max_length=512):
    """
    Generates an SQL query from a natural language question using a T5 model.
    
    Parameters:
        model_path (str): Path to the pre-trained model.
        question (str): Natural language question.
        max_length (int): Maximum length of the generated SQL query.

    Returns:
        str: Generated SQL query.
    """
    schema = (
        '"airlines" "IATA_CODE" text , "AIRLINE" text , primary key: "IATA_CODE" [SEP] '
        '"airports" "IATA_CODE" text , "AIRPORT" text , "CITY" text , "STATE" text , "COUNTRY" text , "LATITUDE" real , "LONGITUDE" real , '
        'primary key: "IATA_CODE" [SEP] '
        '"flights" "YEAR" int , "MONTH" int , "DAY" int , "DAY_OF_WEEK" int , "AIRLINE" text , "FLIGHT_NUMBER" text , "TAIL_NUMBER" text , '
        '"ORIGIN_AIRPORT" text , "DESTINATION_AIRPORT" text , "SCHEDULED_DEPARTURE" int , "DEPARTURE_TIME" int , "DEPARTURE_DELAY" int , '
        '"TAXI_OUT" int , "WHEELS_OFF" int , "SCHEDULED_TIME" int , "ELAPSED_TIME" int , "AIR_TIME" int , "DISTANCE" int , "WHEELS_ON" int , '
        '"TAXI_IN" int , "SCHEDULED_ARRIVAL" int , "ARRIVAL_TIME" int , "ARRIVAL_DELAY" int , "DIVERTED" int , "CANCELLED" int , '
        '"CANCELLATION_REASON" text , "AIR_SYSTEM_DELAY" int , "SECURITY_DELAY" int , "AIRLINE_DELAY" int , "LATE_AIRCRAFT_DELAY" int , "WEATHER_DELAY" int , '
        'foreign_key: "AIRLINE" from "airlines" "IATA_CODE" , foreign_key: "ORIGIN_AIRPORT" from "airports" "IATA_CODE" , '
        'foreign_key: "DESTINATION_AIRPORT" from "airports" "IATA_CODE" , primary key: "YEAR" "MONTH" "DAY" "FLIGHT_NUMBER" [SEP]'
    )
    
    # Load model and tokenizer
    model_path = 'gaussalgo/T5-LM-Large-text2sql-spider'
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    
    # Prepare input text
    input_text = f"Question: {question} Schema: {schema}"
    
    # Tokenize input
    model_inputs = tokenizer(input_text, return_tensors="pt")
    
    # Generate output
    outputs = model.generate(**model_inputs, max_length=max_length)
    
    # Decode output to text
    output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    
    return output_text

# Example usage
if __name__ == "__main__":
    question = "What is the average arrival delay for each airline?"    
    sql_query = generate_sql_query(question)
    print("SQL Query:", sql_query)
