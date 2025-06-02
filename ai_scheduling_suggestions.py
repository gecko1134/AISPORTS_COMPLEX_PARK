
def recommend_slot_allocations(requests, available_slots):
    recommendations = []
    for request in requests:
        for slot in available_slots:
            if slot['type'] == request['type'] and not slot['filled']:
                recommendations.append({'team': request['team'], 'slot': slot['id']})
                slot['filled'] = True
                break
    return recommendations
