import math

class PoincareBallGeometry:
    """Poincare Ball manifold distance and operations."""
    def distance(self, u: list[float], v: list[float]) -> dict:
        norm_u_sq = sum(x ** 2 for x in u)
        norm_v_sq = sum(x ** 2 for x in v)
        diff_sq = sum((x - y) ** 2 for x, y in zip(u, v))

        # Clamp norms inside open unit ball
        norm_u_sq = min(norm_u_sq, 0.9999)
        norm_v_sq = min(norm_v_sq, 0.9999)

        delta = 1.0 + (2.0 * diff_sq) / ((1.0 - norm_u_sq) * (1.0 - norm_v_sq))
        d_p = math.acosh(max(1.0, delta))

        return {
            "u": u,
            "v": v,
            "hyperbolic_distance": round(d_p, 5)
        }
