from client import PoincareBallGeometry

def main():
    print("=== Poincare Ball Hyperbolic Geometry ===")
    pbg = PoincareBallGeometry()
    res = pbg.distance([0.1, 0.2], [0.3, 0.4])
    print("Hyperbolic distance result:", res)
    assert res["hyperbolic_distance"] > 0.0

    print("Poincare Ball Geometry verified successfully!")

if __name__ == "__main__":
    main()
