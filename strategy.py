def Signal(InputRow):
    SignalLine = []
    if InputRow['SMA_high_5_5Min'] >= 0 and InputRow['SMA_low_5_5Min'] >= 0:
        if InputRow['high'] >= InputRow['SMA_high_5_5Min']:
            SignalLine.append({'type': 'buy', 'price': InputRow['close'], 'stop_loss_price': 0.995*InputRow['close']})

        if InputRow['low'] <= InputRow['SMA_low_5_5Min']:
            SignalLine.append({'type': 'sell', 'price': InputRow['close'], 'stop_loss_price': 1.005*InputRow['close']})

    if len(SignalLine) > 1:
        return []
    else:
        return SignalLine