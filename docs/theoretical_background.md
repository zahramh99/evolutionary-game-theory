# Theoretical Foundations

## Evolutionary Game Theory
- **Prisoner's Dilemma Payoff Matrix**:
  |               | Cooperate | Defect |
  |---------------|-----------|--------|
  | **Cooperate** | (3, 3)    | (0, 5) |
  | **Defect**    | (5, 0)    | (1, 1) |

- **Key Strategies**:
  - TFT (Tit-for-Tat): Mirror opponent's last move
  - Pavlov: Cooperates if both agreed last round

## Metrics
- **Cooperation Rate**: 
  $$ C_t = \frac{N_{Cooperate}}{N_{Total}} $$
- **Strategy Entropy**:
  $$ H = -\sum p_i \log_2 p_i $$